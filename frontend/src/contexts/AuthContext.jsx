import { createContext, useContext, useEffect, useState } from "react"
import { loginUser } from "../services/auth"

const AuthContext = createContext()

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null)

  useEffect(() => {
    // Load user from localStorage on initial load
    const token = localStorage.getItem("access_token")
    if (token) {
      // TODO: Fetch user profile
    }
  }, [])

  const login = async (email, password) => {
    const data = await loginUser({ email, password })
    localStorage.setItem("access_token", data.access)
    localStorage.setItem("refresh_token", data.refresh)
    setUser({ email })
  }

  const logout = () => {
    localStorage.removeItem("access_token")
    localStorage.removeItem("refresh_token")
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => useContext(AuthContext)