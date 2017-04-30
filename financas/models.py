from django.db import models
from django.utils import timezone


class Endereco(models.Model):
	nomeRua = models.CharField(max_length=100)
	bairro = models.CharField(max_length=100)
	numero = models.CharField(max_length=50)
	cep = models.CharField(max_length=8)
	municipio = models.CharField(max_length=100)
	uf = models.CharField(max_length=2)


	def __str__(self):
		return self.nomeRua + ', ' + self.bairro + ', ' + self.numero + ', ' + self.cep + ', ' + self.municipio + ', ' + self.uf 

	class Meta:
		verbose_name_plural = "Endereço"


class Pessoa(models.Model):
	email = models.EmailField(default=None)


class PessoaFisica(Pessoa):
	nomeCompleto = models.CharField(max_length=200)
	cpf = models.CharField(max_length=14)
	endereco = models.ForeignKey(Endereco)

	def __str__(self):
		return self.nomeCompleto + ', CPF: ' + self.cpf

	class Meta:
		verbose_name_plural = "Pessoa física"


class PessoaJuridica(Pessoa):
	razaoSocial = models.CharField(max_length=200)
	inscricaoEstadual = models.CharField(max_length=50)
	inscricaoMunicipal = models.CharField(max_length=50)
	cnpj = models.CharField(max_length=20)
	endereco = models.ForeignKey(Endereco)
	titular = models.ForeignKey(PessoaFisica)

	def __str__(self):
		return self.razaoSocial + ', CNPJ: ' + self.cnpj

	class Meta:
		verbose_name_plural = "Pessoa jurídica"


class Empresas(models.Model):
	identificacao = models.CharField(max_length=50)
	endereco = models.ForeignKey(Endereco)
	pessoaJuridica = models.ForeignKey(PessoaJuridica)

	def __str__(self):
		return self.identificacao

	class Meta:
		verbose_name_plural = "Empresas"


class Fornecedor(models.Model):
	identificacao = models.CharField(max_length=50)
	classificacao = models.CharField(max_length=18)
	endereco = models.ForeignKey(Endereco)
	funcao = models.CharField(max_length=50)

	def __str__(self):
		return self.identificacao +', ' + self.classificacao +', ' + self.funcao


class FornecedorPessoaFisica(Fornecedor):
	pessoaFisica = models.ForeignKey(PessoaFisica)

	class Meta:
		verbose_name_plural = "Fornecedor pessoa física"

	def __str__(self):
		return self.pessoaFisica.nomeCompleto


class FornecedorPessoaJuridica(Fornecedor):
	pessoaJuridica = models.ForeignKey(PessoaJuridica)

	def __str__(self):
  		return self.pessoaJuridica.razaoSocial

class Meta:
	verbose_name_plural = "Fornecedor pessoa jurídica"


class Cliente(models.Model):
	identificacao = models.CharField(max_length=50, default=None)
	classificacao = models.CharField(max_length=18, default=None)
	endereco = models.ForeignKey(Endereco, default=None)
	funcao = models.CharField(max_length=50, default=None)

	def __str__(self):
		return self.identificacao + ', ' + self.classificacao


class ClientePessoaFisica(Cliente):
	pessoaFisica = models.ForeignKey(PessoaFisica)

	def __str__(self):
		return self.pessoaFisica

	class Meta:
		verbose_name_plural = "Cliente pessoa física"


class ClientePessoaJuridica(Cliente):
	pessoaJuridica = models.ForeignKey(PessoaJuridica)

	def __str__(self):
		return self.pessoaJuridica

	class Meta:
		verbose_name_plural = "Cliente pessoa jurídica"


class ContasBancarias(models.Model):
	classificacao = models.CharField(max_length=18)
	descricao = models.CharField(max_length=50)
	numeroConta = models.CharField(max_length=20)
	numeroAgencia = models.CharField(max_length=20)
	dataSaldoInicial = models.CharField(max_length=12)
	saldoInicial = models.CharField(max_length=14)
	caixa = models.CharField(max_length=1)
	banco = models.CharField(max_length=1)

	def __str__(self):
		return self.numeroConta + ', ' + self.numeroAgencia + ', ' + self.banco

	class Meta:
		verbose_name_plural = "Conta bancária"


class PlanoDeContas(models.Model):
	contaBancaria = models.ForeignKey(ContasBancarias)
	classificacao = models.CharField(max_length=18)
	tipoConta = models.CharField(max_length=15)
	descricao = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	entradaSaida = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Plano de contas"

	def __str__(self):
		return self.contaBancaria+ ', '+self.classificacao+ ', '+self.tipoConta+ ', '+self.descricao+ ', '+self.tipo+ ', '+self.entradaSaida


class FormasDePagamento(models.Model):
	descricao = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Formas de pagamento"

	def __str__(self):
		return self.descricao


class LancamentosAReceber(models.Model):
	cliente = models.ForeignKey(Cliente)
	empresa = models.ForeignKey(Empresas)
	dataVencimento = models.DateTimeField(default=timezone.now)
	dataEmissao = models.DateTimeField(default=timezone.now)
	valorTitulo = models.CharField(max_length=14)
	numeroDocumento = models.CharField(max_length=20)

	class Meta:
		verbose_name_plural = "Lançamentos a receber"

	def __str__(self):
		return self.cliente+ ', '+self.empresa+ ', '+self.dataVencimento+ ', '+self.valorTitulo+ ', '+self.numeroDocumento


class BaixasAReceber(models.Model):
	formaDePagamento = models.ForeignKey(FormasDePagamento)
	lancamentosAReceber = models.ForeignKey(LancamentosAReceber)
	banco = models.CharField(max_length=50)
	disponibilidade = models.DateTimeField(default=timezone.now)
	dataBaixa = models.DateTimeField(default=timezone.now)
	valorPago = models.CharField(max_length=14)
	residual = models.CharField(max_length=14)

	class Meta:
		verbose_name_plural = "Baixas a receber"

	def __str__(self):
		return self.formaDePagamento+ ', '+self.lancamentosAReceber+ ', '+self.banco+ ', '+self.disponibilidade+ ', '+self.dataBaixa+ ', '+self.valorPago


class LancamentosAPagar(models.Model):
	fornecedor = models.ForeignKey(Fornecedor)
	empresa = models.ForeignKey(Empresas)
	dataVencimento = models.DateTimeField(default=timezone.now)
	dataEmissao = models.DateTimeField(default=timezone.now)
	valorTitulo = models.CharField(max_length=14)
	numeroDocumento = models.CharField(max_length=20)

	class Meta:
		verbose_name_plural = "Lançamentos a pagar"

	def __str__(self):
		return sself.empresa+ ', '+self.dataVencimento+ ', '+self.dataEmissao+ ', '+self.valorTitulo

class BaixasAPagar(models.Model):
	formaDePagamento = models.ForeignKey(FormasDePagamento)
	lancamentosAPagar = models.ForeignKey(LancamentosAPagar)
	banco = models.CharField(max_length=50)
	disponibilidade = models.DateTimeField(default=timezone.now)
	dataBaixa = models.DateTimeField(default=timezone.now)
	valorPago = models.CharField(max_length=14)
	residual = models.CharField(max_length=14)

	class Meta:
		verbose_name_plural = "Baixas a pagar"

	def __str__(self):
		return self.formaDePagamento+ ', '+self.lancamentosAPagar+ ', '+self.banco+ ', '+self.disponibilidade+ ', '+self.dataBaixa+ ', '+self.valorPago+', '+self.residual



class Tesouraria(models.Model):
	empresa = models.ForeignKey(Empresas)
	cliente = models.ForeignKey(Cliente)
	planoDeContas = models.ForeignKey(PlanoDeContas)
	formaDePagamento = models.ForeignKey(FormasDePagamento)
	fornecedor = models.ForeignKey(Fornecedor)
	valor = models.CharField(max_length=14)
	numero = models.CharField(max_length=15)
	dataEmissao = models.DateTimeField(default=timezone.now)
	dataVencimento = models.DateTimeField(default=timezone.now)
	dataDisponibilidade = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Tesouraria"

	def __str__(self):
		return self.empresa+ ', '+self.cliente+ ', '+self.formaDePagamento+ ', '+self.valor+', '+self.numero+', '+self.dataVencimento
