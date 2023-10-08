import styles from './CadastroclienteForm.module.css'
import axios from 'axios'
import SubmitButton from '../../form/SubmitButton'
import { useParams } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'

function DeletarperfilForm() {

    const navigate = useNavigate()
    const { id } = useParams()
    const handleSubmit = data => {
        data.preventDefault()

        const tokenauth = localStorage.getItem('token')
        const auth = { 'Authentication': `${tokenauth}` }
        axios.delete(`http://localhost:5000/user/${id}`, { headers: auth }).then((res) => { if (res.data.message) { navigate('/deletarperfil/:id') } else { navigate('/login') } }).catch(err => console.log(err))

    }

    return (
        <div>
            <form className={styles.form} onSubmit={handleSubmit}>
                <SubmitButton text="Deletar perfil permanentemente" />
            </form>
        </div>
    )
}

export default DeletarperfilForm