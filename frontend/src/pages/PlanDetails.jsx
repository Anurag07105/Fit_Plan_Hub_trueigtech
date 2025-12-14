import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/axios";

export default function PlanDetails() {
  const { id } = useParams();
  const [plan, setPlan] = useState(null);

  useEffect(() => {
    api.get(`/plans/${id}`).then((res) => setPlan(res.data));
  }, [id]);

  if (!plan) return null;

  return (
    <div>
      <h2>{plan.title}</h2>
      <p>{plan.access === "full" ? plan.description : "Subscribe to unlock full plan"}</p>

      {plan.access === "preview" && (
        <button onClick={() => api.post(`/plans/${id}/subscribe`)}>
          Subscribe
        </button>
      )}
    </div>
  );
}
