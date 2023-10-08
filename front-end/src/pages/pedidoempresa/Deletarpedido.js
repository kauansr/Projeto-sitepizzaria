import DeletarpedidoEmpresaForm from '../../components/project/DeletarpedidoEmpresaForm'
import style from '../../styles/Logincliente.module.css'
import styles from '../../components/layout/Navbar.module.css'
import { Link } from 'react-router-dom'

function Deletarpedidoempresa() {

    return (
        <div><nav className={styles.navbar}>
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
                <h1>tem certeza que deseja apagar pedido do cliente ?</h1>
                <DeletarpedidoEmpresaForm />
            </div></div>
    )
}

export default Deletarpedidoempresa