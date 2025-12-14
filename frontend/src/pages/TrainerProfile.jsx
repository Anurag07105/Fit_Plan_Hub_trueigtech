import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/axios";
import PlanCard from "../components/PlanCard";

export default function TrainerProfile() {
  const { id } = useParams();
  const [trainer, setTrainer] = useState(null);
  const [plans, setPlans] = useState([]);
  const [following, setFollowing] = useState(false);

  useEffect(() => {
    api.get(`/trainer/${id}`).then(res => {
      setTrainer(res.data.trainer);
      setPlans(res.data.plans);
      setFollowing(res.data.following);
    });
  }, [id]);

  const toggleFollow = async () => {
    if (following) {
      await api.post(`/trainer/${id}/unfollow`);
    } else {
      await api.post(`/trainer/${id}/follow`);
    }
    setFollowing(!following);
  };

  if (!trainer) return null;

  return (
    <div>
      <h2>{trainer.name}</h2>
      <button onClick={toggleFollow}>
        {following ? "Unfollow" : "Follow"}
      </button>

      <h3>Plans</h3>
      {plans.map(plan => (
        <PlanCard key={plan.id} plan={plan} preview />
      ))}
    </div>
  );
}
