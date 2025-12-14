function Landing() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">
        Available Fitness Plans
      </h1>

      <div className="grid md:grid-cols-3 gap-6">
        {[1, 2, 3].map((plan) => (
          <div
            key={plan}
            className="bg-white rounded-xl shadow p-6 hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold mb-2">
              Fat Loss Beginner Plan
            </h2>
            <p className="text-gray-600 mb-4">
              30-day plan designed for beginners
            </p>
            <p className="font-bold text-indigo-600 mb-4">₹999</p>

            <button className="w-full bg-indigo-600 text-white py-2 rounded hover:bg-indigo-700">
              View Details
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Landing;
