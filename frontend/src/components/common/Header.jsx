import Link from "next/link"
import { useRouter } from "next/router"
import { useTranslation } from "next-i18next"
import { useAuth } from "../../contexts/AuthContext"
import CartButton from "./CartButton"
import LanguageSwitcher from "./LanguageSwitcher"

export default function Header() {
  const { t } = useTranslation("common")
  const { user, logout } = useAuth()
  const router = useRouter()

  return (
    <header className="bg-white shadow-sm">
      <nav className="container mx-auto px-4 py-4 flex justify-between items-center">
        <Link href="/" className="text-2xl font-bold text-primary">
          DesertThreads
        </Link>

        <div className="flex items-center gap-6">
          <div className="flex gap-4">
            <Link href="/products/category/kaftans" className="hover:text-primary">
              {t("categories.kaftans")}
            </Link>
            <Link href="/products/category/abayas" className="hover:text-primary">
              {t("categories.abayas")}
            </Link>
          </div>

          <div className="flex items-center gap-4">
            <CartButton />
            <LanguageSwitcher />
            {user ? (
              <button onClick={logout} className="hover:text-primary">
                {t("logout")}
              </button>
            ) : (
              <Link href="/login" className="hover:text-primary">
                {t("login")}
              </Link>
            )}
          </div>
        </div>
      </nav>
    </header>
  )
}