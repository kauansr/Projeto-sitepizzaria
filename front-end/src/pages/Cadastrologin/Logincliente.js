import style from '../../styles/Logincliente.module.css'
import LoginclienteForm from "../../components/project/LoginclienteForm"
import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'


function Logincliente() {
    return (


        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>
                    <li className={styles.item}>
                        <Link to="/cadastrocliente">Cadastrar</Link>
                    </li>


                    <li className={styles.item}>
                        <Link to="/cadastroempresa">Cadastrar empresa</Link>

                    </li>
                </ul>
            </nav>
            <div className={style.logincliente_container}>
                <h1>Login</h1>
                <LoginclienteForm />
            </div></div>
    )
}

export default Logincliente