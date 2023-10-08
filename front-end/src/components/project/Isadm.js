import { Navigate } from "react-router-dom"
import { Outlet } from "react-router-dom"



const Isadmin = () => {

    const is_admin = localStorage.getItem("is_admin")


    return is_admin ? <Outlet /> : <Navigate to="/produtos" />




}

export default Isadmin