import axios from "axios";
import { jwtDecode } from "jwt-decode";
import dayjs from "dayjs";
import { useNavigate } from "react-router-dom";

const baseURL = "https://shopcrawl-server.onrender.com";

const useAxios = () => {
  const navigate = useNavigate();
  let authTokens = localStorage.getItem("authTokens")
    ? JSON.parse(localStorage.getItem("authTokens"))
    : null;

  const axiosInstance = axios.create({
    baseURL,
    headers: { Authorization: `Bearer ${authTokens?.access}` },
  });

  axiosInstance.interceptors.request.use(async (req) => {
    if (!authTokens) {
      authTokens = localStorage.getItem("authTokens")
        ? JSON.parse(localStorage.getItem("authTokens"))
        : null;

      if (authTokens) {
        req.headers.Authorization = `Bearer ${authTokens.access}`;
      } else {
        navigate("/login");
        throw new Error("No auth tokens found. Please log in again.");
      }
    }

    const user = jwtDecode(authTokens.access);
    const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;

    if (isExpired) {
      localStorage.removeItem("authTokens");
      navigate("/login");
      throw new Error("Token expired. Please log in again.");
    }

    return req;
  });

  return axiosInstance;
};

export default useAxios;
