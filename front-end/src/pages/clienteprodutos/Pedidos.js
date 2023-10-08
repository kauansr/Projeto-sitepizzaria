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
            const res = await axios.get("http://localhost:5000/pedidos", { headers: { 'Authentication': `${tokenauth}` } })



            setPosts(res.data.pedidos)
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

                    </li>
                    <li className={styles.item}>
                        <Link to="/produtos">Produtos</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/perfil">Perfil</Link>

                    </li>
                </ul>

            </nav>
            {posts.length === 0 ? <p>Vazio...</p> : (
                posts.map((post) => (
                    <div key={post.id} className={style.post}>
                        <div>
                            <h2>{post.nome}</h2>
                            <h3>  {post.email}
                            </h3>
                            <h3>data do pedido: {post.data_pedido}</h3>
                            <h3>Status: {post.status}</h3>
                            <h3>frete: {post.frete}</h3>
                            <h3>preco total: {post.custo_total}</h3>
                            <br></br>
                            <div>
                                <Link to={`/deletarpedido/${post.id}`}> <SubmitButton text="Cancelar" /> </Link>
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