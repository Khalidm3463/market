import { useRouter } from "next/router"
import useSWR from "swr"
import ProductCard from "../../../../components/common/ProductCard"
import api from "../../../../services/api"

const fetcher = (url) => api.get(url).then(res => res.data)

export default function CategoryPage() {
  const router = useRouter()
  const { slug } = router.query

  const { data: products, error } = useSWR(
    slug ? `/products/products/?category=${slug}` : null,
    fetcher
  )

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8 capitalize">
        {slug?.replace("-", " ")}
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {products?.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  )
}