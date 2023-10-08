import DeletarpedidoForm from '../../components/project/DeletarpedidoForm'
import style from '../../styles/Logincliente.module.css'
import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'

function Deletarpedido() {

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
            <div className={style.logincliente_container}>
                <h1>tem certeza que deseja apagar pedido ?</h1>
                <DeletarpedidoForm />
            </div></div>
    )
}

export default Deletarpedido