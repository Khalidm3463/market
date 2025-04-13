import Link from "next/link"
import Image from "next/image"
import { formatPrice } from "../../utils/formatPrice"

export default function ProductCard({ product }) {
  return (
    <div className="border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow">
      <Link href={`/products/${product.id}`}>
        <div className="aspect-square relative">
          <Image
            src={product.image || "/placeholder-clothing.jpg"}
            alt={product.name}
            fill
            className="object-cover"
          />
        </div>
        <div className="p-4">
          <h3 className="font-medium text-lg">{product.name}</h3>
          <p className="text-gray-600 text-sm mb-2">
            {product.category?.name}
          </p>
          <div className="flex justify-between items-center">
            <span className="text-primary font-bold">
              {formatPrice(product.price, "AED")}
            </span>
          </div>
        </div>
      </Link>
    </div>
  )
}
