import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'
import style from '../../styles/Logincliente.module.css'
import AtualizarperfilempresaForm from '../../components/project/AtualizarperfilempresaForm'

function Atualizarperfilempresa() {

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
                        <Link to="/perfilempresa">Perfil</Link>

                    </li>
                </ul>

            </nav>
            <div className={style.logincliente_container}>
                <h1>Atualizar Perfil da empresa</h1>
                <AtualizarperfilempresaForm />
            </div></div>
    )
}

export default Atualizarperfilempresa