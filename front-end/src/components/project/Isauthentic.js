import { Navigate } from "react-router-dom"
import { Outlet } from "react-router-dom"



const IsAuthenticated = () => {

    const is_authenticated = localStorage.getItem("token")

    return is_authenticated ? <Outlet /> : <Navigate to="/login" />


}

export default IsAuthenticated