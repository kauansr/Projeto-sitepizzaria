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
            const res = await axios.get("http://localhost:5000/user/empresa", { headers: { 'Authentication': `${tokenauth}` } })


            if (res.data.users) {
                setPosts(res.data.users)
            }
            else {
                setPosts(res.data.message)

            }


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
                        <Link to="/admin/verpedidosempresa">Pedidos</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/admin/produtoscrudempresa">Produtos da empresa</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/perfil">Perfil</Link>

                    </li>
                </ul>

            </nav>

            {posts.length === 0 ? <p>Carregando...</p> : (
                posts.map((post) => (
                    <div key={post.id} className={style.post}>
                        <div>
                            <h3>Empresa: {post.empresa}</h3>

                            <h3>cnpj:  {post.cnpj}
                            </h3>
                            <h3>Id de usuario: {post.user_id}</h3>
                            <h3>ID empresa: {post.id}</h3>
                            <br></br>
                            <div>
                                <Link to={`/admin/atualizarperfilempresa/${post.id}`}> <SubmitButton text="Atualizar" /> </Link>
                            </div><br></br>
                            <div>
                                <Link to={`/admin/deletarperfilempresa/${post.id}`}> <SubmitButton text="Deletar empresa" /> </Link>
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