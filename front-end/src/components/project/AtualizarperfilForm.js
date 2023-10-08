import styles from './CadastroclienteForm.module.css'
import { useState } from 'react'
import axios from 'axios'
import SubmitButton from '../../form/SubmitButton'
import Input from '../../form/Input'
import { useParams, useNavigate } from 'react-router-dom'

function AtualizarperfilForm() {


    const data = { name: "", email: "", age: 0 }
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
        axios.put(`http://localhost:5000/user/${id}`, dataInput, { headers: auth }).then((res) => { if (res.data.message) { navigate('/atualizarperfil/:id') } else { navigate('/perfil') } }).catch(err => console.log(err))
    }

    return (
        <div>
            <form className={styles.form} onSubmit={handleSubmit}>
                <Input type="text" text="Nome" name="name" handleOnChange={handleFormChange} placeholder="Insira o nome" />
                <Input type="number" step={1} min={1} text="Idade" name="age" handleOnChange={handleFormChange} placeholder="Insira a idade" />
                <Input type="text" text="E-mail" name="email" handleOnChange={handleFormChange} placeholder="Insira o email" />
                <SubmitButton text="Atualizar perfil" />
            </form>
        </div>
    )
}

export default AtualizarperfilForm