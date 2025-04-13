// import { appWithTranslation } from "next-i18next"
// import { AuthProvider } from "../contexts/AuthContext"
// import Header from "../components/common/Header"
// import "../styles/globals.css"
// import { CartProvider } from "../contexts/CartContext"

// function App({ Component, pageProps }) {
//   return (
//     <AuthProvider>
//       <div className="min-h-screen">
//         <Header />
//         <main className="pb-16">
//           <Component {...pageProps} />
//         </main>
//       </div>
//     </AuthProvider>
//   )
// }

// export default appWithTranslation(App)


import { appWithTranslation } from "next-i18next"
import { AuthProvider } from "../contexts/AuthContext"
import { CartProvider } from "../contexts/CartContext" // ✅ Import this
import Header from "../components/common/Header"
import "../styles/globals.css"

function App({ Component, pageProps }) {
  return (
    <AuthProvider>
      <CartProvider> {/* ✅ Wrap the rest of the app */}
        <div className="min-h-screen">
          <Header />
          <main className="pb-16">
            <Component {...pageProps} />
          </main>
        </div>
      </CartProvider>
    </AuthProvider>
  )
}

export default appWithTranslation(App)
