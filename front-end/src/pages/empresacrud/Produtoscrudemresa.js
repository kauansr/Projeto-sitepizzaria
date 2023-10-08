import axios from "axios"
import { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import SubmitButton from "../../form/SubmitButton"
import styles from '../../components/layout/Navbar.module.css'
import style from '../../styles/Post.module.css'

function Produtoscrudempresa() {

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
                        <Link to="/admin/cadastrarproduto">Cadastrar produto</Link>

                    </li>


                    <li className={styles.item}>
                        <Link to="/admin/verpedidosempresa">Ver pedidos empresa</Link>

                    </li><li className={styles.item}>
                        <Link to="/perfil">Perfil</Link>

                    </li></ul></nav>
            <h1>Produtos</h1>
            {posts.length === 0 ? <p>Vazio...</p> : (
                posts.map((post) => (
                    <div key={post.id} className={style.post} >
                        <div>
                            <h2>  {post.nome_produto}
                            </h2>

                            <h3>preco: {post.produto_preco}</h3>

                            <div>
                                <Link to={`/admin/atualizarprodutos/${post.id}`}> <SubmitButton text="Atualizar" /> </Link>
                            </div><br></br>
                            <div>
                                <Link to={`/admin/deletarprodutos/${post.id}`}> <SubmitButton text="Deletar" /> </Link>
                            </div><br></br> <br></br>
                            <div>
                                <Link to="/admin/cadastrarproduto"> <SubmitButton text="Novo produto" /> </Link>
                            </div><br></br>
                        </div>
                    </div>


                ))
            )
            }
        </div >
    )
}

export default Produtoscrudempresa