import styles from './CadastroempresaForm.module.css'
import { useState } from 'react'
import axios from 'axios'
import SubmitButton from '../../form/SubmitButton'
import Input from '../../form/Input'
import { useNavigate } from 'react-router-dom'


function CadastroempresaForm() {

    const data = { email: "", name: "", age: 0, empresa: "", cnpj: "", password: "" }
    const [dataInput, setDataInput] = useState(data)

    const handleFormChange = (e) => {
        setDataInput({ ...dataInput, [e.target.name]: e.target.value })

    }

    const navigate = useNavigate()
    function handleSubmit(e) {
        e.preventDefault()
        axios.post("http://localhost:5000/user/empresa", dataInput).then((res) => { if (res.data.message) { navigate('/cadastroempresa') } else { navigate('/login') } }).catch(err => console.log(err))

    }

    return (
        <div>
            <form className={styles.form} onSubmit={handleSubmit}  >
                <Input type="email" text="Email" name="email" handleOnChange={handleFormChange} placeholder="Insira seu E-mail" />
                <Input type="text" text="Nome" name="name" handleOnChange={handleFormChange} placeholder="Insira seu nome" />
                <Input type="number" text="Idade" name="age" handleOnChange={handleFormChange} placeholder="Insira sua idade" />
                <Input type="text" text="Cnpj" name="cnpj" handleOnChange={handleFormChange} placeholder="Insira seu Cnpj" />
                <Input type="text" text="Empresa" name="empresa" handleOnChange={handleFormChange} placeholder="Insira o nome da empresa" />
                <Input type="password" text="Senha" name="password" handleOnChange={handleFormChange} placeholder="Insira sua senha" />
                <SubmitButton text="Cadastrar" />
            </form>

        </div>
    )
}

export default CadastroempresaForm