import { useRouter } from "next/router"
import useSWR from "swr"
import api from "../../../services/api"

const fetcher = (url) => api.get(url).then(res => res.data)

export default function ProductDetailPage() {
  const router = useRouter()
  const { id } = router.query

  const { data: product, error } = useSWR(
    id ? `/products/products/${id}/` : null,
    fetcher
  )

  if (!product) return <div>Loading...</div>
  if (error) return <div>Error loading product</div>

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid md:grid-cols-2 gap-8">
        {/* Image Gallery */}
        <div className="grid gap-4">
          <div className="aspect-square relative rounded-lg overflow-hidden">
            <img
              src={product.image || "/placeholder-clothing.jpg"}
              alt={product.name}
              className="object-cover w-full h-full"
            />
          </div>
        </div>

        {/* Product Info */}
        <div className="space-y-4">
          <h1 className="text-3xl font-bold">{product.name}</h1>
          <p className="text-2xl text-primary">
            {formatPrice(product.price, "AED")}
          </p>
          
          <div className="space-y-2">
            <h3 className="font-medium">Size Guide</h3>
            <pre>{JSON.stringify(product.size_guide, null, 2)}</pre>
          </div>

          <button className="bg-primary text-white px-6 py-3 rounded-full">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  )
}