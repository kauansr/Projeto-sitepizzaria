import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'
import style from '../../styles/Logincliente.module.css'
import AtualizarperfilForm from '../../components/project/AtualizarperfilForm'

function Atualizarperfil() {

    return (
        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>
                    <li className={styles.item}>
                        <Link to="/pedidos">Pedidos</Link>

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
                <h1>Atualizar Perfil</h1>
                <AtualizarperfilForm />
            </div></div>
    )
}

export default Atualizarperfil