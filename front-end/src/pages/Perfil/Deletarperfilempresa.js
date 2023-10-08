import DeletarperfilempresaForm from '../../components/project/DeletarperfilempresaForm'
import style from '../../styles/Logincliente.module.css'
import styles from '../../components/layout/Navbar.module.css'
import { Link } from 'react-router-dom'

function Deletarperfilempresa() {

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
                    <Link to="/perfilempresa">Perfil</Link>

                </li>
            </ul>

        </nav>
            <div className={style.logincliente_container}>
                <h1>tem certeza que deseja apagar a sua empresa  ?</h1>
                <DeletarperfilempresaForm />
            </div></div>
    )
}

export default Deletarperfilempresa