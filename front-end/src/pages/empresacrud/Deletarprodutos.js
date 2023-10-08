import DeletarprodutosForm from '../../components/project/DeletarprodutosForm'
import style from '../../styles/Logincliente.module.css'
import styles from '../../components/layout/Navbar.module.css'
import { Link } from 'react-router-dom'

function Deletarprodutos() {

    return (
        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>
                    <li className={styles.item}>
                        <Link to="/verpedidosempresa">Pedidos</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/produtoscrudempresa">Produtos da empresa</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/perfil">Perfil</Link>

                    </li>
                </ul>

            </nav>
            <div className={style.logincliente_container}>
                <h1>tem certeza que deseja deletar produto ?</h1>
                <DeletarprodutosForm />
            </div></div>
    )
}

export default Deletarprodutos