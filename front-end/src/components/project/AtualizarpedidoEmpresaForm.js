import styles from './CadastroclienteForm.module.css'
import { useState } from 'react'
import axios from 'axios'
import SubmitButton from '../../form/SubmitButton'
import Input from '../../form/Input'
import { useParams } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'

function AtualizarprodutoForm() {


    const data = { 'Preparando...': "", 'Enviado': "", 'Entregue': "" }
    const [dataInput, setDataInput] = useState(data)

    const handleFormChange = (e) => {
        setDataInput({ ...dataInput, [e.target.name]: e.target.value })

    }

    const navigate = useNavigate()
    const { id } = useParams()
    const handleSubmit = data => {
        data.preventDefault()

        const tokenauth = localStorage.getItem('token')
        const auth = { 'Authentication': `${tokenauth}` }
        axios.put(`http://localhost:5000/user/empresa/pedido/${id}`, dataInput, { headers: auth }).
            then((res) => { if (res.data.message) { navigate('/admin/atualizarpedidoempresa/:id') } else { navigate('/admin/verpedidosempresa') } }).catch(err => console.log(err))

    }

    return (
        <div>
            <form className={styles.form} onSubmit={handleSubmit}>
                <button type='submit' name='Entregue' value='Entregue' onClick={handleFormChange}>Entregue</button>
                <button type='submit' name='Enviado' value='Enviado' onClick={handleFormChange}>Enviado</button>
                <button type='submit' name="Preparando..." value='Preparando...' onClick={handleFormChange}>Preparando...</button>

            </form>
        </div>
    )
}

export default AtualizarprodutoForm