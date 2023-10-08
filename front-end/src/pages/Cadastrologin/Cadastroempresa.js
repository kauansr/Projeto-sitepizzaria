import CadastroempresaForm from "../../components/project/CadastroempresaForm"
import style from '../../styles/Logincliente.module.css'
import { Link } from "react-router-dom"
import styles from '../../components/layout/Navbar.module.css'

function Cadastroempresa() {
    return (

        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>
                    <li className={styles.item}>
                        <Link to="/cadastrocliente">Cadastrar</Link>
                    </li>

                    <li className={styles.item}>
                        <Link to="/">Login</Link>

                    </li>

                </ul>
            </nav>
            <div className={style.logincliente_container}>
                <h1>Cadastro empresa</h1>
                <CadastroempresaForm />
            </div></div>
    )
}

export default Cadastroempresa