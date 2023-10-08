import axios from "axios"
import { useState, useEffect } from "react"
import SubmitButton from "../../form/SubmitButton"
import { Link } from "react-router-dom"
import styles from '../../components/layout/Navbar.module.css'
import style from '../../styles/Post.module.css'

function Produtos() {

    const [posts, setPosts] = useState([])

    const getPosts = async () => {

        try {

            const tokenauth = localStorage.getItem('token')
            const res = await axios.get("http://localhost:5000/user/empresa/produtos", { headers: { 'Authentication': `${tokenauth}` } })



            setPosts(res.data.Produto)

        } catch (error) {
            console.log(error)

        }


    }


    useEffect(() => {
        getPosts()
    }, [])



    return (
        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>
                    <li className={styles.item}>
                        <Link to="/pedidos">Meus pedidos</Link>

                    </li><li className={styles.item}>
                        <Link to="/perfil">Perfil</Link>

                    </li></ul>

            </nav>

            {posts.length === 0 ? <p>Vazio</p> : (
                posts.map((post) => (
                    <div key={post.id} className={style.post}>
                        <div>
                            <h2>  {post.nome_produto}
                            </h2>
                            <h3>Preco: {post.produto_preco} R$</h3>
                            <br></br>
                            <div>
                                <Link to={`/produto/${post.id}`}> <SubmitButton text="Ver" /> </Link>
                            </div><br></br>

                        </div>
                    </div>

                ))
            )
            }
        </div >
    )
}

export default Produtos