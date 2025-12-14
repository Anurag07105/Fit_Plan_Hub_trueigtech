function TrainerDashboard() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">Trainer Dashboard</h1>

      <div className="bg-white shadow rounded p-6">
        <p className="text-gray-600 mb-4">
          Manage your fitness plans here.
        </p>

        <button className="bg-indigo-600 text-white px-4 py-2 rounded">
          + Create New Plan
        </button>
      </div>
    </div>
  );
}

export default TrainerDashboard;
