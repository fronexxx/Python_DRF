import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const pizzaService = {
    getAll() {
        return apiService.get(urls.pizzas)
    },

    create(data) {
        return apiService.post(urls.pizzas, {pizza_shop_id: 1}, ...data)
    },
};

export {
    pizzaService
}