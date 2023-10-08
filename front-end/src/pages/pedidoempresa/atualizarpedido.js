import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'
import style from '../../styles/Logincliente.module.css'
import AtualizarpedidoEmpresaForm from '../../components/project/AtualizarpedidoEmpresaForm'

function Atualizarpedidoempresa() {

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
                <h1>Atualizar pedido</h1>
                <AtualizarpedidoEmpresaForm />
            </div></div>
    )
}

export default Atualizarpedidoempresa