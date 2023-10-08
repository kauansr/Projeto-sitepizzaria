import DeletarperfilForm from '../../components/project/DeletarperfilForm'
import style from '../../styles/Logincliente.module.css'
import styles from '../../components/layout/Navbar.module.css'
import { Link } from 'react-router-dom'

function Deletarperfil() {

    return (
        <div><nav className={styles.navbar}>
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
                <h1>tem certeza que deseja apagar a sua conta  ?</h1>
                <DeletarperfilForm />
            </div></div>
    )
}

export default Deletarperfil