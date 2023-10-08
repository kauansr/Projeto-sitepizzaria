import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Logincliente from './pages/Cadastrologin/Logincliente';
import Cadastrocliente from './pages/Cadastrologin/Cadastrocliente'
import Cadastroempresa from './pages/Cadastrologin/Cadastroempresa'
import Produtos from './pages/clienteprodutos/Produtos';
import Produtosempresa from './pages/empresacrud/Produtosempresa';
import Atualizarprodutos from './pages/empresacrud/Atualizasprodutos';
import Produtoscrudempresa from './pages/empresacrud/Produtoscrudemresa';
import Deletarprodutos from './pages/empresacrud/Deletarprodutos';
import Deletarpedido from './pages/clienteprodutos/Deletarpedido'
import Pedidos from './pages/clienteprodutos/Pedidos';
import Pedidosempresa from './pages/pedidoempresa/Pedidosempresa';
import Atualizarpedidoempresa from './pages/pedidoempresa/atualizarpedido';
import Deletarpedidoempresa from './pages/pedidoempresa/Deletarpedido';
import Perfilcli from './pages/Perfil/Perfilcli'
import Atualizarperfil from './pages/Perfil/Atualizarperfil'
import Deletarperfil from './pages/Perfil/Deletarperfil'
import Perfilempresa from './pages/Perfil/perfilempresa'
import Atualizarperfilempresa from './pages/Perfil/Atualizarperfilempresa'
import Deletarperfilempresa from './pages/Perfil/Deletarperfilempresa'
import Isadmin from './components/project/Isadm';
import IsAuthenticated from './components/project/Isauthentic';
import UmProduto from './pages/clienteprodutos/Produto';

function App() {



  return (
    <div>
      <Router>

        <Routes>
          <Route exact path="/login" element={<Logincliente />} />
          <Route exact path="/cadastrocliente" element={<Cadastrocliente />} />
          <Route exact path="/cadastroempresa" element={<Cadastroempresa />} />

          <Route path='/' element={<IsAuthenticated />}>




            <Route path="/admin" element={<Isadmin />}>
              <Route exact path="cadastrarproduto" element={<Produtosempresa />} />
              <Route exact path="produtoscrudempresa" element={<Produtoscrudempresa />} />

              <Route exact path="atualizarprodutos/:id" element={<Atualizarprodutos />} />
              <Route exact path="deletarprodutos/:id" element={<Deletarprodutos />} />


              <Route exact path="atualizarpedidoempresa/:id" element={<Atualizarpedidoempresa />} />
              <Route exact path="deletarpedidoempresa/:id" element={<Deletarpedidoempresa />} />
              <Route exact path="verpedidosempresa" element={<Pedidosempresa />} />


              <Route exact path="deletarperfilempresa/:id" element={<Deletarperfilempresa />} />
              <Route exact path="atualizarperfilempresa/:id" element={<Atualizarperfilempresa />} />
              <Route exact path="perfilempresa" element={<Perfilempresa />} />

              <Route exact path="cadastrarproduto" element={<Produtosempresa />} />
              <Route exact path="produtoscrudempresa" element={<Produtoscrudempresa />} />

              <Route exact path="atualizarprodutos/:id" element={<Atualizarprodutos />} />
              <Route exact path="deletarprodutos/:id" element={<Deletarprodutos />} />


              <Route exact path="atualizarpedidoempresa/:id" element={<Atualizarpedidoempresa />} />
              <Route exact path="deletarpedidoempresa/:id" element={<Deletarpedidoempresa />} />
              <Route exact path="verpedidosempresa" element={<Pedidosempresa />} />


              <Route exact path="deletarperfilempresa/:id" element={<Deletarperfilempresa />} />
              <Route exact path="atualizarperfilempresa/:id" element={<Atualizarperfilempresa />} />
              <Route exact path="perfilempresa" element={<Perfilempresa />} /> </Route>




            <Route exact path="perfil" element={<Perfilcli />} />
            <Route exact path="atualizarperfil/:id" element={<Atualizarperfil />} />
            <Route exact path="deletarperfil/:id" element={<Deletarperfil />} />


            <Route exact path="deletarpedido/:id" element={<Deletarpedido />} />
            <Route exact path="pedidos" element={<Pedidos />} />

            <Route exact path="produtos" element={<Produtos />} />
            <Route exact path="produto/:id" element={<UmProduto />} />
          </Route>

        </Routes>
      </Router>

    </div >
  );
}

export default App;
