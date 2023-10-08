import styles from './CadastroclienteForm.module.css'
import { useState } from 'react'
import axios from 'axios'
import SubmitButton from '../../form/SubmitButton'
import Input from '../../form/Input'
import { useNavigate } from 'react-router-dom'


function CadastroclienteForm() {

    const data = { email: "", name: "", age: 0, password: "" }
    const [dataInput, setDataInput] = useState(data)

    const handleFormChange = (e) => {
        setDataInput({ ...dataInput, [e.target.name]: e.target.value })

    }

    const navigate = useNavigate()
    function handleSubmit(e) {
        e.preventDefault()
        axios.post("http://localhost:5000/user", dataInput).then((res) => { if (res.data.message) { navigate('/cadastrocliente') } else { navigate('/login') } }).catch(err => console.log(err))
    }

    return (
        <div>
            <form className={styles.form} onSubmit={handleSubmit}  >
                <Input type="email" text="Email" name="email" handleOnChange={handleFormChange} placeholder="Insira seu E-mail" />
                <Input type="text" text="Nome" name="name" handleOnChange={handleFormChange} placeholder="Insira seu nome" />
                <Input type="number" text="Idade" name="age" handleOnChange={handleFormChange} placeholder="Insira sua idade" />
                <Input type="password" text="Senha" name="password" handleOnChange={handleFormChange} placeholder="Insira sua senha" />
                <SubmitButton text="Cadastrar" />
            </form>

        </div>
    )
}

export default CadastroclienteForm