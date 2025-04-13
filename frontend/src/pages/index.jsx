import useSWR from "swr"
import { useTranslation } from "next-i18next"
// import ProductCard from "../../components/common/ProductCard.jsx"
import ProductCard from "../components/common/ProductCard.jsx"

// import api from "../../services/api"
import api from "../services/api.js"

const fetcher = (url) => api.get(url).then(res => res.data)

export default function HomePage() {
  const { t } = useTranslation("common")
  const { data: products, error } = useSWR(
    "/products/products/?category=kaftans", 
    fetcher
  )

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">{t("homepage.title")}</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {products?.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  )
}