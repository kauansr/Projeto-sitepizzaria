import styles from './CadastroclienteForm.module.css'
import { useState } from 'react'
import axios from 'axios'
import SubmitButton from '../../form/SubmitButton'
import Input from '../../form/Input'
import { useNavigate } from 'react-router-dom'

function CadastrarprodutosForm() {


    const data = { produto_nome: "", produto_preco: 0.0 }
    const [dataInput, setDataInput] = useState(data)

    const handleFormChange = (e) => {
        setDataInput({ ...dataInput, [e.target.name]: e.target.value })

    }

    const navigate = useNavigate()

    function handleSubmit(e) {
        e.preventDefault()
        const tokenauth = localStorage.getItem('token')
        const auth = { 'Authentication': `${tokenauth}` }
        axios.post("http://localhost:5000/user/empresa/produtos", dataInput, { headers: auth }).then((res) => { if (res.data.message) { navigate('/admin/cadastrarproduto') } else { navigate('/admin/produtoscrudempresa') } }).catch(err => console.log(err))
    }

    return (
        <div>
            <form className={styles.form} onSubmit={handleSubmit}>
                <Input type="text" text="Nome" name="produto_nome" handleOnChange={handleFormChange} placeholder="Insira o nome do produto" />
                <Input type="number" step={0.01} min={0.01} text="Preco" name="produto_preco" handleOnChange={handleFormChange} placeholder="Insira o preco do produto" />
                <SubmitButton text="Cadastrar produto" />
            </form>
        </div>
    )
}

export default CadastrarprodutosForm