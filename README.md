# Abstract Factory

## Definição do GoF, no livro "Padrões de Projeto" (2000)

### Intenção: 
Fornecer uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar 
suas classes concretas.

### Tipo de pattern:
Criação

### Também conhecido como:
Kit

### Aplicável quando:
- Um sistema deve ser independente de como seus produtos são criados, compostos ou representados
- Um sistema deve ser configurado como um produto de uma família de múltiplos produtos
- Uma família de objetos-produtos for projetada para ser usada em conjunto e você necessita garantir essa restrição
- Você quer fornecer uam biblioteca de classes de produtos e quer revelar somente suas interfaces, não suas implementações

### Participantes:
- **AbstractFactory:** Interface para as operações que criam os objetos-produto abstratos
- **ConcreteFactory:** Implementações da interface **AbstractFactory**
- **AbstractProduct:** Interface que representa um tipo objeto-produto a ser "produzido" por alguma implementação de  **AbstractFactory**
- **ConcreteProduct:** Implementações da interface ConcreteProduct, defininido um objeto-produto a ser criado pela **ConcreteFactory** correspondente
- **Client**: Consome as Factories e Products somente via interfaces (**AbstractFactory** e **AbstractProduct**)


##




