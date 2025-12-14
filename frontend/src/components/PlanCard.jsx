import { Link } from "react-router-dom";

export default function PlanCard({ plan, preview }) {
  return (
    <div style={{ border: "1px solid #ccc", margin: 10, padding: 10 }}>
      <h3>{plan.title}</h3>
      <p>Price: ₹{plan.price}</p>

      {preview ? (
        <Link to={`/plans/${plan.id}`}>View Preview</Link>
      ) : (
        <p>{plan.description}</p>
      )}
    </div>
  );
}
