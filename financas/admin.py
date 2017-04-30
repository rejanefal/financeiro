from django.contrib import admin
from . import models


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['nomeRua', 'bairro', 'numero', 'cep', 'municipio', 'uf']


class EmpresasAdmin(admin.ModelAdmin):
	list_display = ['identificacao', 'endereco', 'pessoaJuridica']


class PessoaFisicaAdmin(admin.ModelAdmin):
	list_display = ['nomeCompleto', 'cpf', 'endereco', 'email']


class PessoaJuridicaAdmin(admin.ModelAdmin):
	list_display = ['razaoSocial', 'inscricaoEstadual', 'inscricaoMunicipal', 'cnpj', 'titular', 'email']


class FornecedorPessoaFisicaAdmin(admin.ModelAdmin):
	list_display = ['identificacao', 'classificacao', 'endereco', 'pessoaFisica', 'funcao']


class FornecedorPessoaJuridicaAdmin(admin.ModelAdmin):
	list_display = ['identificacao', 'classificacao', 'endereco', 'pessoaJuridica', 'funcao']


class ClientePessoaFisicaAdmin(admin.ModelAdmin):
	list_display = ['pessoaFisica', 'identificacao', 'classificacao', 'funcao']


class ClientePessoaJuridicaAdmin(admin.ModelAdmin):
	list_display = ['pessoaJuridica', 'identificacao', 'classificacao', 'funcao']


class ContasBancariasAdmin(admin.ModelAdmin):
	list_display = ['numeroConta', 'numeroAgencia', 'banco', 'descricao', 'caixa']


class PlanoDeContasAdmin(admin.ModelAdmin):
	list_display = ['contaBancaria', 'classificacao', 'tipoConta', 'descricao']


class FormasDePagamentoAdmin(admin.ModelAdmin):
	list_display = ['descricao']


class LancamentosAReceberAdmin(admin.ModelAdmin):
	list_display = ['cliente', 'empresa', 'dataVencimento', 'dataEmissao', 'valorTitulo', 'numeroDocumento']


class BaixasAReceberAdmin(admin.ModelAdmin):
	list_display = ['formaDePagamento', 'lancamentosAReceber', 'banco', 'disponibilidade', 'dataBaixa', 'valorPago', 'residual']


class LancamentosAPagarAdmin(admin.ModelAdmin):
	list_display = ['fornecedor', 'empresa', 'dataVencimento', 'dataEmissao', 'valorTitulo', 'numeroDocumento']


class BaixasAPagarAdmin(admin.ModelAdmin):
	list_display = ['formaDePagamento', 'lancamentosAPagar', 'banco', 'disponibilidade', 'dataBaixa', 'valorPago', 'residual']


class TesourariaAdmin(admin.ModelAdmin):
	list_display = ['empresa', 'cliente', 'planoDeContas', 'formaDePagamento', 'fornecedor', 'valor', 'numero', 'dataEmissao', 'dataVencimento', 'dataDisponibilidade']


admin.site.register(models.Endereco, EnderecoAdmin)
admin.site.register(models.Empresas, EmpresasAdmin)
admin.site.register(models.PessoaFisica, PessoaFisicaAdmin)
admin.site.register(models.PessoaJuridica, PessoaJuridicaAdmin)
admin.site.register(models.FornecedorPessoaFisica, FornecedorPessoaFisicaAdmin)
admin.site.register(models.FornecedorPessoaJuridica, FornecedorPessoaJuridicaAdmin)
admin.site.register(models.ClientePessoaFisica, ClientePessoaFisicaAdmin)
admin.site.register(models.ClientePessoaJuridica, ClientePessoaJuridicaAdmin)
admin.site.register(models.ContasBancarias, ContasBancariasAdmin)
admin.site.register(models.PlanoDeContas, PlanoDeContasAdmin)
admin.site.register(models.FormasDePagamento, FormasDePagamentoAdmin)
admin.site.register(models.LancamentosAReceber, LancamentosAReceberAdmin)
admin.site.register(models.BaixasAReceber, BaixasAReceberAdmin)
admin.site.register(models.LancamentosAPagar, LancamentosAPagarAdmin)
admin.site.register(models.BaixasAPagar, BaixasAPagarAdmin)
admin.site.register(models.Tesouraria, TesourariaAdmin)