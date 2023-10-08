import axios from "axios"
import { useState, useEffect } from "react"
import SubmitButton from "../../form/SubmitButton"
import { Link, useNavigate, useParams } from "react-router-dom"
import styles from '../../components/layout/Navbar.module.css'
import style from '../../styles/Post.module.css'

function UmProduto() {

    const [posts, setPosts] = useState([])

    const navigate = useNavigate()
    const { id } = useParams()


    const getPost = async () => {

        try {

            const tokenauth = localStorage.getItem('token')
            const res = await axios.get(`http://localhost:5000/user/empresa/produtos/${id}`, { headers: { 'Authentication': `${tokenauth}` } })



            setPosts(res.data.produto)



        } catch (error) {
            console.log(error)

        }


    }


    useEffect(() => {
        getPost()
    }, [])

    const handleSubmit = data => {
        data.preventDefault()
        const tokenauth = localStorage.getItem('token')
        const auth = { 'Authentication': `${tokenauth}` }
        axios.post(`http://localhost:5000/pedidos/${id}`, {}, { headers: auth }).then((res) => { if (res.data.message) { navigate('/produtos') } else { navigate('/pedidos') } }).catch(err => console.log(err))
    }

    return (
        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>
                    <li className={styles.item}>
                        <Link to="/pedidos">Meus pedidos</Link>

                    </li><li className={styles.item}>
                        <Link to="/perfil">Perfil</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/produtos">Produtos</Link>

                    </li>
                </ul>

            </nav>

            {posts.length === 0 ? <p>Vazio...</p> : (

                <div className={style.post}>
                    <div key={posts.id}>
                        <h2> {posts.produto_nome}
                        </h2>
                        <h3>Preco: {posts.produto_preco} R$</h3>
                        <br></br>
                        <div>
                            <form onSubmit={handleSubmit}>
                                <SubmitButton text='Pedir' />
                            </form>
                        </div><br></br>

                    </div>
                </div>

            )

            }
        </div >
    )
}

export default UmProduto