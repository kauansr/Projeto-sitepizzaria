import styles from './SubmitButton.module.css'
import { useState, useEffect } from "react"
import axios from 'axios'


function SubmitButton({ text }) {
    return (
        <div >
            <button className={styles.btn} type='submit'
            >{text}</button>
        </div>
    )

}
export default SubmitButton