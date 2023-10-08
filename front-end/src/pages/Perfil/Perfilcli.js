import axios from "axios"
import { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import SubmitButton from "../../form/SubmitButton"
import styles from '../../components/layout/Navbar.module.css'
import style from '../../styles/Post.module.css'

function Pedidos() {

    const [posts, setPosts] = useState([])

    const getPosts = async () => {

        try {

            const tokenauth = localStorage.getItem('token')
            const res = await axios.get("http://localhost:5000/user", { headers: { 'Authentication': `${tokenauth}` } })



            setPosts(res.data.users)
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
                        <Link to="/produtos">Produtos</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/pedidos">Pedidos</Link>

                    </li>
                </ul>

            </nav>

            {posts.length === 0 ? <p>Carregando...</p> : (
                posts.map((post) => (
                    <div key={post.id} className={style.post}>
                        <div>
                            <h3>Nome: {post.name}</h3>

                            <h3>E-mail:  {post.email}
                            </h3>
                            <h3>Idade: {post.age}</h3>
                            <br></br>
                            <div>
                                <Link to={`/atualizarperfil/${post.id}`}> <SubmitButton text="Atualizar" /> </Link>
                            </div><br></br>
                            <div>
                                <Link to={`/deletarperfil/${post.id}`}> <SubmitButton text="Deletar conta" /> </Link>
                            </div><br></br>
                            <div>
                                <Link to={`/admin/perfilempresa`}> <SubmitButton text="perfil da empresa" /> </Link>
                            </div><br></br>

                        </div>
                    </div>

                ))
            )
            }
        </div >
    )
}

export default Pedidos