import Link from "next/link"
import { useCart } from "../../contexts/CartContext"

export default function CartButton() {
  const { items } = useCart()
  
  return (
    <Link href="/cart" className="relative hover:text-primary">
      🛒 Cart
      {items.length > 0 && (
        <span className="absolute -top-2 -right-4 bg-primary text-white text-xs w-5 h-5 rounded-full flex items-center justify-center">
          {items.length}
        </span>
      )}
    </Link>
  )
}