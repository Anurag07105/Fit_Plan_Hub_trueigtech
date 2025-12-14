function Feed() {
  return (
    <div className="p-8 bg-gray-50 min-h-screen">
      <h1 className="text-3xl font-bold mb-6 text-gray-800">
        Your Personalized Feed
      </h1>

      <div className="grid md:grid-cols-2 gap-6">
        {[1, 2].map((item) => (
          <div
            key={item}
            className="bg-white rounded-xl shadow p-6 hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold mb-2">
              Strength Training Plan
            </h2>

            <p className="text-gray-600 mb-3">
              By Trainer: <span className="font-medium">Anurag Joshi</span>
            </p>

            <p className="text-indigo-600 font-bold mb-4">
              Subscribed 
            </p>

            <button className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700">
              Continue Plan
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Feed;
