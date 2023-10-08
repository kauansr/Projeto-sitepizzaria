import styles from './CadastroclienteForm.module.css'
import { useState } from 'react'
import axios from 'axios'
import SubmitButton from '../../form/SubmitButton'
import Input from '../../form/Input'
import { useParams, useNavigate } from 'react-router-dom'

function AtualizarperfilempresaForm() {


    const data = { cnpj: "", empresa: "" }
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
        axios.put(`http://localhost:5000/user/empresa/${id}`, dataInput, { headers: auth }).then((res) => { if (res.data.message) { navigate('/admin/atualizarperfilempresa/:id') } else { navigate('/admin/perfilempresa') } }).catch(err => console.log(err))
    }

    return (
        <div>
            <form className={styles.form} onSubmit={handleSubmit}>
                <Input type="text" text="Cnpj" name="cnpj" handleOnChange={handleFormChange} placeholder="Insira o cnpj" />
                <Input type="text" text="Empresa" name="empresa" handleOnChange={handleFormChange} placeholder="Insira o empresa" />
                <SubmitButton text="Atualizar perfil empresa" />
            </form>
        </div>
    )
}

export default AtualizarperfilempresaForm