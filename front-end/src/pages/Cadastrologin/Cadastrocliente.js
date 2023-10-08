import CadastroclienteForm from '../../components/project/CadastroclienteForm'
import style from '../../styles/Logincliente.module.css'
import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'

function Cadastrocliente() {
    return (

        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>

                    <li className={styles.item}>
                        <Link to="/">Login</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/cadastroempresa">Cadastrar empresa</Link>

                    </li>
                </ul>
            </nav>
            <div className={style.logincliente_container}>
                <h1>Cadastrar</h1>
                <CadastroclienteForm />
            </div></div>
    )
}

export default Cadastrocliente