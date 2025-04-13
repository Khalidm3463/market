import { useRouter } from "next/router"
import { useTranslation } from "next-i18next"

export default function LanguageSwitcher() {
  const { i18n } = useTranslation()
  const router = useRouter()

  const changeLanguage = (locale) => {
    const { pathname, asPath, query } = router
    router.push({ pathname, query }, asPath, { locale })
  }

  return (
    <div className="flex gap-2">
      <button
        onClick={() => changeLanguage("en")}
        className={`px-2 py-1 rounded ${i18n.language === "en" ? "bg-primary text-white" : ""}`}
      >
        EN
      </button>
      <button
        onClick={() => changeLanguage("ar")}
        className={`px-2 py-1 rounded ${i18n.language === "ar" ? "bg-primary text-white" : ""}`}
      >
        AR
      </button>
    </div>
  )
}