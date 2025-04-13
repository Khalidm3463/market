import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api"

const api = axios.create({
    baseURL: API_URL,
    headers: {
      "Content-Type": "application/json",
    },
  })


// Add JWT token to requests
api.interceptors.request.use((config) => {
    const token = localStorage.getItem("access_token")
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  })
  
  export default api