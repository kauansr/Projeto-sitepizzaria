import AtualizarprodutosForm from '../../components/project/AtualizarprodutoForm'
import style from '../../styles/Logincliente.module.css'
import { Link } from 'react-router-dom'
import styles from '../../components/layout/Navbar.module.css'

function Atualizarprodutos() {

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
                <h1>Atualizar produto</h1>
                <AtualizarprodutosForm />
            </div></div>
    )
}

export default Atualizarprodutos