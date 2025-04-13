import { useState } from "react"
import { useCart } from "../contexts/CartContext"
import api from "../services/api"

export default function CheckoutPage() {
  const { items, total } = useCart()
  const [address, setAddress] = useState("")
  const [loading, setLoading] = useState(false)

  const handleCheckout = async () => {
    setLoading(true)
    try {
      const { data } = await api.post("/orders/orders/", {
        items: items.map(item => ({
          product: item.id,
          quantity: item.quantity
        })),
        delivery_address: address,
        total_price: total
      })
      
      // Handle payment initiation
      const paymentResponse = await api.post("/payments/initiate/", {
        order_id: data.id,
        method: "TELR" // or "COD"
      })

      if (paymentResponse.data.payment_url) {
        window.location.href = paymentResponse.data.payment_url
      }
    } catch (error) {
      console.error("Checkout failed:", error)
    }
    setLoading(false)
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Checkout</h1>
      
      <div className="grid md:grid-cols-2 gap-8">
        <div className="space-y-6">
          <div>
            <label className="block mb-2 font-medium">Delivery Address</label>
            <textarea
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              className="w-full p-3 border rounded-lg"
              placeholder="Enter your full address"
              required
            />
          </div>
        </div>

        <div className="bg-gray-50 p-6 rounded-lg">
          <h2 className="text-xl font-bold mb-4">Order Summary</h2>
          {items.map(item => (
            <div key={item.id} className="flex justify-between mb-2">
              <span>{item.name} x{item.quantity}</span>
              <span>{formatPrice(item.price * item.quantity, "AED")}</span>
            </div>
          ))}
          <div className="border-t pt-4 mt-4">
            <div className="flex justify-between font-bold">
              <span>Total</span>
              <span>{formatPrice(total, "AED")}</span>
            </div>
          </div>
          <button
            onClick={handleCheckout}
            disabled={loading || !address}
            className="bg-primary text-white w-full py-3 rounded-full mt-6 disabled:opacity-50"
          >
            {loading ? "Processing..." : "Confirm Order"}
          </button>
        </div>
      </div>
    </div>
  )
}