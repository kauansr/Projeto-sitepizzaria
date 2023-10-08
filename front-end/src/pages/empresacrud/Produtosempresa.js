import CadastrarprodutosForm from '../../components/project/CadastrarprodutosForm'
import style from '../../styles/Logincliente.module.css'
import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'

function Produtosempresa() {

    return (
        <div>
            <nav className={styles.navbar}>
                <ul className={styles.list}>
                    <li className={styles.item}>
                        <Link to="/admin/verpedidosempresa">Pedidos</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/admin/produtoscrudempresa">Produtos da empresa</Link>

                    </li>
                    <li className={styles.item}>
                        <Link to="/perfil">Perfil</Link>

                    </li>
                </ul>

            </nav>
            <div className={style.logincliente_container}>
                <h1>Cadastrar produto</h1>
                <CadastrarprodutosForm />
            </div></div>
    )
}

export default Produtosempresa