import api from "../api/api";

export async function loginStart(data) {
    const response = await api.post("/auth/login/start", data);
    return response.data;
}

export async function loginFinish(data) {
    const response = await api.post("/auth/login/finish", data);
    return response.data;
}