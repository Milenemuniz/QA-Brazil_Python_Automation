import data
import helpers


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        """Verifica a conectividade com o servidor do Urban Routes antes dos testes."""
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        """Prepara o teste para definir a rota."""
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_select_plan(self):
        """Prepara o teste para selecionar o plano."""
        print("função criada para selecionar o plano")
        # Adicionar em S8
        pass

    def test_fill_phone_number(self):
        """Prepara o teste para preencher o número de telefone."""
        print("função criada para preencher o telefone")
        # Adicionar em S8
        pass

    def test_fill_card(self):
        """Prepara o teste para adicionar o cartão de crédito."""
        print("função criada para adicionar o cartão")
        # Adicionar em S8
        pass

    def test_comment_for_driver(self):
        """Prepara o teste para adicionar comentário ao motorista."""
        print("função criada para adicionar comentário")
        # Adicionar em S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        """Prepara o teste para pedir cobertor e lenços."""
        print("função criada para pedir cobertor e lenços")
        # Adicionar em S8
        pass

    def test_order_2_ice_creams(self):
        """Prepara o teste para pedir 2 sorvetes usando um ciclo for."""
        print("função criada para pedir 2 sorvetes")
        for _ in range(2):
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        """Prepara o teste para verificar a busca do carro."""
        print("função criada para verificar a busca do carro")
        # Adicionar em S8
        pass