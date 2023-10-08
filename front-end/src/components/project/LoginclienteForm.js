import SubmitButton from '../../form/SubmitButton'
import Input from '../../form/Input'
import styles from '../project/LoginclienteForm.module.css'
import React, { useState, useEffect } from "react"
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

function LoginclienteForm() {

    const data = { email: "", password: "" }
    const [dataInput, setDataInput] = useState(data)

    const navigate = useNavigate()

    const handleFormChange = (e) => {
        setDataInput({ ...dataInput, [e.target.name]: e.target.value })

    }



    function handleSubmit(e) {
        e.preventDefault()
        axios.post("http://localhost:5000/login", dataInput).then((res) => {

            if (res.data) {


                if (res.data[0] !== 0) {
                    if (res.data[1]['is_admin'] == true) {
                        localStorage.setItem('is_admin', res.data[1]['is_admin'])
                        localStorage.setItem('token', res.data[0]['token'])
                        navigate('/admin/cadastrarproduto')
                    }
                    else {
                        localStorage.setItem('token', res.data[0]['token'])
                        localStorage.removeItem('is_admin')
                        navigate('/produtos')
                    }
                }
                else {
                    localStorage.removeItem('token')
                    navigate('/login')
                }


            }
            else {
                localStorage.removeItem('token')
                navigate('/login')
            }

        })
            .catch(err => console.log(err))
    }

    return (

        <form className={styles.form} onSubmit={handleSubmit}  >
            <Input type="email" text="Email" name="email" handleOnChange={handleFormChange} placeholder="Insira seu E-mail" />
            <Input type="password" text="Senha" name="password" handleOnChange={handleFormChange} placeholder="Insira sua senha" />
            <SubmitButton text="Entrar" />
        </form>

    )
}

export default LoginclienteForm